from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Document, Module
from .serializers import ModuleSerializer, DocumentSerializer

from django.conf import settings
import google.generativeai as genai



prompt = """Generate 10 multiple-choice question (MCQ) based on the text provided. The question should be:

- Relevant to the core concepts or details in the text.
- Clear and concise, suitable for a university-level assignment.
- Designed so that the correct answer is not immediately obvious from the question alone.
- Accompanied by 4 plausible answer options, all of which should be grammatically correct.
- Include the index of the correct answer in the answer field.

Return the result as a JSON object structured as follows:
{
    "question": "QUESTION_TEXT",
    "options": ["OPTION_1", "OPTION_2", "OPTION_3", "OPTION_4"],
    "answer": "CORRECT_OPTION_INDEX"
}
"""


class DocumentView(APIView):
    def get(self, request):
        id = request.query_params.get('id', None)
        documents = Document.objects.all().filter(module=id) if id else Document.objects.all()
        documents = DocumentSerializer(documents, many=True).data
        random_document = {"id": -1, "docfile": "Random", "module": -1}
        documents.insert(0, random_document)
        return Response({"documents": documents})
    
class AddDocumentView(APIView):
    def post(self, request):
        file = request.data['file']
        module = request.data['module']

        module = Module.objects.get(id=module)
        filename = request.data['file'].name
        with open(f'documents/{filename}', 'wb+') as f:
            f.write(file.read())
        
        document = Document(docfile=f'documents/{filename}', module=module)
        document.save()

        return Response({"document": "added"})
    


class ModuleView(APIView):
    def get(self, request):
        modules = Module.objects.all()
        modules = ModuleSerializer(modules, many=True).data
        random_module = {"id": -1, "key": "random", "name": "Random", "credits": 0}
        modules.insert(0, random_module)
        return Response({"modules": modules})
    
    def post(self, request):
        module = Module(key=request.data['key'], name=request.data['name'], credits=request.data['credits'])
        module.save()
        return Response({"module": module.id})
    
class QuestionsView(APIView):
    def get(self, request):
        selected_module = int(request.query_params.get('module', -1))
        selected_document = int(request.query_params.get('document', -1))

        print(selected_module, selected_document)

        if selected_module == -1:
            document = Document.objects.order_by('?').first()
        
        else:
            if selected_document == -1:
                document = Document.objects.filter(module=selected_module).order_by('?').first()
            else:
                document = Document.objects.get(id=selected_document)
        
        genai.configure(api_key=settings.GEMINI_API_KEY)
        document_content = document.docfile.read()

        model = genai.GenerativeModel(settings.AI_MODEL)
        prompt_with_data = f"{document_content}\n\n{prompt}"

        result = model.generate_content([prompt_with_data])

        response = result.text
        response = response.replace('```json\n', "")
        response = response.replace('```', "")
        response = response.replace('\n', "")

        json_response = eval(response)
        print(json_response)
        # json_response = {
        #     "question": "QUESTION_TEXT",
        #     "options": ["OPTION_1", "OPTION_2", "OPTION_3", "OPTION_4"],
        #     "answer": 1
        # }

        # json_response = [json_response for i in range(10)]

        
        return Response(json_response)

        
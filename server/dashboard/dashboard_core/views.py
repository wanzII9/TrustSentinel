from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.decorators import api_view
from .models import *
from .serializer import GetSlaveSerializers


# Create your views here.
def index(request):
    context = {'plc_list': PLCList.objects.all()}
    if request.method == 'GET' and 'plc_id' in request.GET:
        get_id = request.GET['plc_id']
        if get_id:
            set_id = PLCList.objects.get(plc_id=get_id)
            slave_list = SlaveDevice.objects.filter(plc_id=set_id)
            context.update({'slave_list': slave_list})

    return render(request, 'index.html', context)


@api_view(['GET'])
def get_slave_check(request):
    context = None
    if request.method == 'GET' and 'plc_id' in request.GET:
        get_id = request.GET['plc_id']
        if get_id:
            set_id = PLCList.objects.get(plc_id=get_id)
            slave_list = SlaveDevice.objects.filter(plc_id=set_id).only('slave_id', 'slave_status')
            if slave_list:
                context = GetSlaveSerializers(slave_list, many=True)
                return Response(context.data)
            
    return Response(context)


class slave_view(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'slave_view.html'

    def get(self, request):
        context = {'plc_list': PLCList.objects.all()}
        if request.method == 'GET' and 'plc_id' in request.GET:
            get_id = request.GET['plc_id']
            if get_id:
                set_id = PLCList.objects.get(plc_id=get_id)
                slave_list = SlaveDevice.objects.filter(plc_id=set_id)
                context.update({'slave_list': slave_list})

        return Response(context)

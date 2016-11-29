from django.shortcuts import render

# Create your views here.


from models import * ;

def list_command(req):
    try:
        res = {} ;
        cmds = command_list.objects.all();
        for cmd in cmds :
            res[str(cmd.key)] = str(cmd.code);
    except :
        print traceback.format_exc();
        raise Http404() ;
    return HttpResponse(json.dumps(res));


def insert_command(req,key,code):
    try:
        res = {} ;
        cmd = command_list.objects.get(key=key);
        if cmd != None :
            res[str(cmd.key)] = str(cmd.code) ;
            cmd.code = code ;
            cmd.save();
        else :
            cmd = command_list(key = key ,code = code);
            cmd.save();
    except :
        print traceback.format_exc();
        raise Http404() ;
    return HttpResponse(json.dumps(res));

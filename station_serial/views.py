#from django.shortcuts import render
from django.http import Http404, HttpResponse
import traceback,json,sys,random ;
# Create your views here.


from models import * ;

def list_command(req):
    try:
        res = [] ;
        cmds = command_list.objects.all();
        for cmd in cmds :
            res.append({"key":str(cmd.key),"code":str(cmd.code)});
            #res[str(cmd.key)] = str(cmd.code);
    except :
        print traceback.format_exc();
        #raise Http404() ;
    return HttpResponse(json.dumps(res));


def insert_command(req):
    try:
        res = {} ;
        inp = req.read();
        if len(inp) > 0 :
            i_cmd = json.loads(str(inp));
            key = i_cmd["key"];
            code = i_cmd["code"];
            try:
                cmd = command_list.objects.get(key=key);
            except:
                cmd = None ;
            if cmd != None :
                res[str(cmd.key)] = str(cmd.code) ;
                cmd.code = code ;
                cmd.save();
            else :
                cmd = command_list(key = key ,code = code);
                cmd.save();
    except :
        print traceback.format_exc();
        #raise Http404() ;
    return HttpResponse(json.dumps(res));

def delete_command(req):
    try:
        res = {} ;
        inp = req.read();
        if len(inp) > 0 :
            cmds = json.loads(inp);
            for cmd in cmds:
                try:
                    tmp = command_list.objects.get(key=cmd) ;
                except:
                    tmp = None ;
                if tmp != None :
                    tmp.delete();
        else :
            command_list.objects.all().delete();
    except:
        print traceback.format_exc();
    return HttpResponse(json.dumps(res));


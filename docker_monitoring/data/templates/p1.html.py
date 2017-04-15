# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1481756139.195913
_enable_loop = True
_template_filename = '/home/mayur/docSnap/Docker_Monitoring/docker_monitoring/docker_monitoring/templates/p1.html'
_template_uri = 'p1.html'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'<html>\n<head>\n\n\n<title>Docker Monitoring System</title>\n<script src="https://code.jquery.com/jquery-3.1.1.js"></script>\n\n<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">\n<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">>\n<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>\n\n<script type="text/javascript">\n    function fetch_details()\n    {\n        host_ip = $("#host_id").val()\n        \n        if(host_ip == ""){\n            window.alert("Enter Some IP address");\n            return\n        }\n        params = {\'host_ip\': host_ip};\n        $.ajax({\n            url: "/docker_controller/get_host_details", \n            data:params,\n            success: function(result){\n                        window.alert("Ajax Success");\n                    }\n        });\n        //write re for checking valid IP\n    }\n</script>\n</head>\n\n\n<body style="background-color:azure">\n    <div id="first-div" style="text-align:center">\n        <img src="https://www.docker.com/sites/default/files/moby.svg" alt="Docker" style="height:200px;">\n        <h1 style="color:#0e2479">DocSnap - Docker Monitoring System</h1>\n    </div>\n    <div style="margin:45px 0px 0px 80px">\n        <label for="host_id" style="font-size:19px">Enter Docker Instance IP Address</label>\n        <div class="input-group input-group-lg" style="width:500px">\n            <input id="host_id" type="text" class="form-control" placeholder="127.0.0.1" aria-describedby="sizing-addon1">\n        </div>\n        <button onclick="fetch_details()" class="btn btn-default" id="details" type="button" style="margin-top:13px;width:125px;height:45px;font-weight:bold;font-size:17px">Get Details</button>\n    </div>\n</body>\n</html>\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"17": 0, "28": 22, "22": 1}, "uri": "p1.html", "filename": "/home/mayur/docSnap/Docker_Monitoring/docker_monitoring/docker_monitoring/templates/p1.html"}
__M_END_METADATA
"""

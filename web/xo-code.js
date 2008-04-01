var XO = window.XO = 
var XO = window.XO = {
    // 
    // Application Hooks
    //
    XO.read_hook:  function() {alert 'read hook is not defined'},
    XO.write_hook: function() {alert 'write hook is not defined'},
    set_status: function (msg) {
        jQuery("#status").html(msg)
    },
    poll_for_command: function () {
        XO.set_status('Polling for a command')
        $.getJSON("/status.json", function(json){
            XO.set_status('Received command: ' + json.command)
            return;
            if (json.command == "read") {
                document.XO_read_hook(json.content)
            }
            else if (json.command == "write") {
                var save_content = document.XO_write_hook()
                $.post("/write", { "content" : save_content })
            }
        })
    }
}


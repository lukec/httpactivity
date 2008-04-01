var XO = window.XO = {
    // 
    // Application Hooks
    //
    read_hook:  function() {alert('read hook is not defined')},
    write_hook: function() {alert('write hook is not defined')},
    set_status: function (msg) {
        jQuery("#status").html(msg)
    },
    poll_for_command: function () {
        XO.set_status('Polling for a command')
        $.getJSON("/status.json", function(json){
            if (json.command == "read") {
                // Content to read, so send it to the application
                XO.read_hook(json.content)
                XO.set_status('Read content from server')
            }
            else if (json.command == "write") {
                // Call the write hook to fetch content, then POST
                // it back to the server
                jQuery.ajax({
                    type: 'POST',
                    url:  '/write',
                    data: { 'save_content': XO.write_hook() },
                    success: function() {
                        XO.set_status('Sent save data to server')
                    }
                })
            }
            else if (json.command == 'idle') {
                XO.set_status('Idle - no command')
            }
            else {
                XO.set_status('Unknown command: ' + json.command)
            }
        })
    }
}

jQuery(function() {XO.poll_for_command()})
setInterval(function() {XO.poll_for_command()}, 10000)

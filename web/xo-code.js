jQuery(function () {
    poller = function () {
        $.getJSON("/status.json", function(json){
            $("<p>Command:" + json.command + "</p>").appendTo("body")
            if (json.command == "read") {
                document.XO_read_hook(json.content)
            }
            else if (json.command == "write") {
                var save_content = document.XO_write_hook()
                $.post("/write", { "content" : save_content })
            }
            else {
                $("<p>Unknown</p>").appendTo("body")
            }
        })
    }

    setInterval( "poller()", 5000 )
})


EVENTS = {
    # SYSTEM EVENTS
    "startup" : {
        "enabled" : True,
        "media": "",
        "message" : "⏰ I just woke up! What are we gonna print today?"
    },
    "shutdown" : {
        "enabled" : True,
        "media": "",
        "message" : "💤 Going to bed now!"
    },
    # PRINTER EVENTS
    "printer_state_operational":{
        "enabled" : True,
        "media": "",
        "message" : "✅ Your printer is operational."
    },
    "printer_state_error":{
        "enabled" : True,
        "media": "",
        "message" : "⚠️ Your printer is in an erroneous state."
    },
    "printer_state_unknown":{
        "enabled" : True,
        "media": "",
        "message" : "❔ Your printer is in an unknown state."
    },
    # PRINTS EVENTS
    "printing_started":{
        "enabled" : True,
        "media": "snapshot",
        "message" : "🖨️ I've started printing **{name}**"
    },
    "printing_paused":{
        "enabled" : True,
        "media": "snapshot",
        "message" : "⏸️ The printing was paused."
    },
    "printing_resumed":{
        "enabled" : True,
        "media": "snapshot",
        "message" : "▶️ The printing was resumed."
    },
    "printing_cancelled":{
        "enabled" : True,
        "media": "snapshot",
        "message" : "🛑 The printing was stopped."
    },
    "printing_done":{
        "enabled" : True,
        "media": "snapshot",
        "message" : "👍 Printing is done! Took about {time_formatted}"
    },
    "printing_failed":{
        "enabled" : True,
        "media": "snapshot",
        "message" : "👎 Printing has failed! :("
    },
    # SD TRANSFERS EVENTS
    "transfer_started":{
        "enabled" : False,
        "media": "thumbnail",
        "message" : "📼 Transfer started: {local} to {remote}"
    },
    "transfer_done":{
        "enabled" : False,
        "media": "",
        "message" : "📼 Transfer done in {time_formatted}"
    },
    "transfer_failed":{
        "enabled" : False,
        "media": "",
        "message" : "📼 Transfer has failed! :("
    },

    # PROGRESS EVENTS
    "printing_progress":{
        "enabled" : True,
        "media": "snapshot",
        "message" : "📢 Printing is at {progress}%",
    },
    "transfer_progress":{
        "enabled" : False,
        "media": "",
        "message" : "📼 Transfer is at {progress}%",
    },

    # TIMELAPSES
    "timelapse_done": {
        "enabled": False,
        "media": "timelapse",
        "message": "🎥 Timelapse has been created: {movie_basename}"
    },
    "timelapse_failed": {
        "enabled": False,
        "media": "",
        "message": "🎥 Timelapse is not available"
    },

    # Not a real message, but we will treat it as one
    "test":{ 
        "enabled" : True,
        "media": "snapshot",
        "message" : "Hello hello! If you see this message, it means that the settings are correct!"
    },
}
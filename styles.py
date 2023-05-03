front_template = """
<div class="media">[sound:{{Video}}]</div>
"""

css = """
.card {
 font-family: arial;
 font-size: 20px;
 text-align: center;
 color: black;
 background-color: white;
}

.expression {
 font-size: 22px;
}

.meaning {
 font-size: 18px;
 color: #000080;
}

.notes {
 font-size: 18px;
}

.media {
 margin: 2px;
}
"""

back_template = """
{{FrontSide}}
<div class="expression">{{Expression}}</div>
<hr>
{{#Meaning}}
<div class="meaning">{{Meaning}}</div>
{{/Meaning}}
<div class="media">[sound:{{Audio}}]</div>
<div class="notes">{{Notes}}</div>
"""

#  ------------------------------------- #

subs2srs_front_template = """
<div class="snapshot">{{Snapshot}}</div>
<div class="expression">{{Expression}}</div>
<div class="media">[sound:{{Audio}}]</div>
"""

subs2srs_css = """
.card {
 font-family: arial;
 font-size: 20px;
 text-align: center;
 color: black;
 background-color: white;
}

.expression {
 font-size: 22px;
}

.meaning {
 font-size: 18px;
 color: #000080;
}

.notes {
 font-size: 18px;
}

.media {
 margin: 2px;
}

.snapshot {
 margin-bottom: 10px;
}

img {
 max-width: 100%;
 height: auto;
}
"""

subs2srs_back_template = """
{{FrontSide}}

{{#Meaning}}
<hr id=answer>
<div class="meaning">{{Meaning}}</div>
{{/Meaning}}
<div class="notes">{{Notes}}</div>
"""

#  ------------------------------------- #

subs2srs_video_front_template = """
<video src="{{Video}}" poster="{{Id}}.jpg" playsinline autoplay onclick="this.currentTime=0;this.play()"></video>

<script>
  var video = document.querySelector('video');
  video.onerror = function() {
    pycmd("ankiplay{{Video}}");
  }
  function playVideo(event) {
    var selection = window.getSelection();
    if (selection.toString().length != 0) {
      return;
    }
    if (typeof pycmd !== 'undefined') {
      pycmd("ankiplay{{Video}}");
    } else {
      video.currentTime = 0;
      video.play();
    }
  }
  document.body.addEventListener("click", playVideo, false);
</script>
"""

subs2srs_video_css = """
.card {
 font-family: arial;
 font-size: 20px;
 text-align: center;
 color: black;
 background-color: white;
}

html {
 height: 100%;
}

body {
 height: calc(100% - 2em);
}

.expression, .meaning {
 margin: 10px;
}

.expression {
 font-size: 22px;
}

.meaning {
 font-size: 18px;
 color: #000080;
}

.notes {
 font-size: 18px;
}

.media {
 margin: 4px;
}

.snapshot {
 margin-bottom: 10px;
}

img {
 max-width: 100%;
 height: auto;
}

video {
 max-width: 100%;
}

.mobile #content {
 margin: 0;
}
"""

subs2srs_video_back_template = """
<video src="{{Video}}" poster="{{Id}}.jpg" playsinline autoplay onclick="this.currentTime=0;this.play()"></video>

<div class="expression">{{Expression}}</div>
{{#Meaning}}
<div class="meaning">{{Meaning}}</div>
{{/Meaning}}
<div class="media">[sound:_.mp3]</div>
<div class="notes">{{Notes}}</div>

<script>
  var video = document.querySelector('video');
  function playVideo(event) {
    var selection = window.getSelection();
    if (selection.toString().length != 0) {
      return;
    }
    if (typeof pycmd !== 'undefined') {
      pycmd("ankiplay{{Video}}");
    } else {
      video.currentTime = 0;
      video.play();
    }
  }
  document.body.addEventListener("click", playVideo, false);

  document.querySelectorAll('.soundLink, .replaybutton').forEach( elm => {
    elm.addEventListener('click', event => event.stopPropagation());
  });

  var elm = document.querySelector('.soundLink, .replaybutton');
  if (elm) {
    var href = elm.getAttribute("href");
    elm.setAttribute('href', href.replace("_.mp3", "{{Audio}}"));
  }
  if (typeof pycmd !== 'undefined') {
    pycmd("ankiplay{{Audio}}");
  }
</script>
"""

#  ------------------------------------- #

subs2srs_audio_front_template = """
<div class="media">[sound:{{Audio}}]</div>
"""

subs2srs_audio_back_template = """
<div class="media">[sound:{{Audio}}]</div>

<hr>

<div class="expression">{{Expression}}</div>
{{#Meaning}}
<div class="meaning">{{Meaning}}</div>
{{/Meaning}}
<div class="notes">{{Notes}}</div>
"""

#  ------------------------------------- #

alternative_front_template = """
<video src="{{Video}}" poster="{{Id}}.jpg" playsinline autoplay onclick="this.currentTime=0;this.play()"></video>
<script>
    window.onkeyup = function(e) {
        var key = e.keyCode ? e.keyCode : e.which;
        if (key == 82) {
            video = document.getElementsByTagName('video')[0];
			video.currentTime=0;
            video.play();
        }
    }
</script>
"""

alternative_css = """
:root {
 --primary-color: black;
 --secondary-color: #555;
 --meaning-color: #000080;
 --background-color: white;
}

/* .nightMode */
:root {
 --primary-color: white;
 --secondary-color: #aaa;
 --meaning-color: #9bc0dd;
 --background-color: #2f2f31;
}

.card {
 font-family: arial;
 font-size: 20px;
 text-align: center;
 color: var(--primary-color);
 background-color: var(--background-color);
}

.expression {
 font-size: 22px;
 color: var(--primary-color);
 margin: 10px 0;
}

.meaning {
 font-size: 18px;
 color: var(--meaning-color);
 margin: 10px 0;
}

.notes {
 color: var(--secondary-color);;
 font-size: 18px;
}

video {
 max-width: 100%;
}

hr#answer {
 margin-top: 12px;
 margin-bottom: 16px;
 height: 1px;
 background-color: #9a9a9a;
 border: none;
}
"""

alternative_back_template = """
{{FrontSide}}

<hr id="answer">

{{#Expression}}
<div class="expression">{{Expression}}</div>
{{/Expression}}

{{#Notes}}
<div class="notes">{{Notes}}</div>
{{/Notes}}

{{#Meaning}}
<div class="meaning">{{Meaning}}</div>
{{/Meaning}}
"""

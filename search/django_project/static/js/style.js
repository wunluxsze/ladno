let watch = document.getElementById('watch');

watch.InnerText = (new Date()).toLocaleTimeString();

setInterval(function() {
   watch.InnerText = (new Date()).toLocaleTimeString();
},1000);


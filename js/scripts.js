
(function () {
  var container = document.getElementById('visualization');

  // start and end not required to be provided
  var options = {
    editable: false,
    width: "100%",
    margin: {
      item: 20,
      axis: 40
    },
    height: 800
  };

  var timeline = new vis.Timeline(container, items, groups, options);
})();

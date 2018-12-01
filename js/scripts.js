
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
    height: 800,
    min: new Date(1920, 0, 0),
    max: new Date(2025, 0, 0),
    zoomMin: 1000 * 60 * 60 * 24 * 31 * 12 * 4, // about 4 years, milliseconds
    tooltip: {
      followMouse: true
    },
    groupOrder: function (a, b) { return a.value - b.value; },
    //groupOrderSwap: function (a, b, groups) { var v = a.value; a.value = b.value; b.value = v; },
    groupTemplate: function(group) {
      var container = document.createElement('div');
      var label = document.createElement('span');
      label.innerHTML = group.content + ' ';
      container.insertAdjacentElement('afterBegin', label);
      var hide = document.createElement('button');
      hide.innerHTML = 'hide';
      hide.style.fontSize = 'small';
      hide.addEventListener('click', function() {
        groups.update({id: group.id, visible: false});
      });
      hide.className = 'btn btn-danger';
      container.insertAdjacentElement('beforeEnd', hide);
      return container;
    }

  };

  var timeline = new vis.Timeline(container, items, groups, options);
})();

function showAllGroups() {
  groups.forEach(function(group) {
    groups.update({id: group.id, visible: true});
  })
};


// note that months are zero-based in the JavaScript Date object
var items = new vis.DataSet([
  // societal events, requiring start and end
  {start: new Date(2001, 9), end: new Date(2011, 9), content: "Post-9-11 Terrorism", type: "background"}, // no group
  {start: new Date(2005, 0), end: new Date(2006, 6), content: "Another background", type: "background", group: 2},

  // films
  {start: new Date(2000, 0), end: new Date(2014, 11), content: "high school"},
  {start: new Date(2011, 0), content: "sophomore year", title: "description here", group: 1},
  {start: new Date(2011, 0), content: "second event", group: 2},
  {start: new Date(2011, 0), content: "third event", group: 2}
]);


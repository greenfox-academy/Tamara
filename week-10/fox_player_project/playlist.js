'use strict';

const Playlists = function() {
  let response = [
    { "id": 1, "title": "Favorites", "system": 1},
    { "id": 2, "title": "Music for programming", "system": 0},
    { "id": 3, "title": "Driving", "system": 0},
    { "id": 5, "title": "Fox house", "system": 0},
  ]
  const playlist = document.querySelector('.leftmenu');
  
  const render = function () {
    response.forEach(function (element) {
      let li = document.createElement('li')
      li.textContent = element.title;
      playlist.appendChild(li);

      let xSign = document.createElement('i');
      xSign.textContent = '<i class="fa fa-times icon" aria-hidden="true"></i>';
      element.push(xSign);
    });
  }
  return {
    render: render
  }
}

let playlistModule = Playlists()
playlistModule.render()
{/*  */}
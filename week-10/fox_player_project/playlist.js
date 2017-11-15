'use strict';

const Playlists = function() {
  let response = [
    { "id": 1, "title": "Favorites", "system": 1},
    { "id": 2, "title": "Music for programming", "system": 0},
    { "id": 3, "title": "Driving", "system": 0},
    { "id": 5, "title": "Fox house", "system": 0},
  ]
  const root = document.querySelector('.leftmenu');
  let actionCallback;
  // const fa = <i class="fa fa-times icon" aria-hidden="true"></i>;
  const render = function() {
    response.forEach(function(element) {
      let li = document.createElement('li')
      li.textContent = element.title;
      root.appendChild(li);  
      // let xSign = document.createElement('i');
      // playlist.appendChild(xSign);
    });
    addEvents();
  }

  const showCreateDialog = function() {}

  const create = function() {
    // let newElement
  }

  // const deleted = function() {
  //   response.forEach(function(element) {
  //     if (element.system === 0) {
  //       let li = root.getElementsByTagName('li');
  //       li.forEach(function(e){
  //         if ()
  //         e.removeChild(li);
  //       })
  //     };
  //     console.log(response);
  //   });
  // };

  const highlight = function(index) {
    let playList = root.querySelectorAll('li');    
    playList.forEach(function(element, i) {
      if (index === i) {
        element.style.backgroundColor = 'lightblue';
      } else if (i % 2 === 0) {
        element.style.backgroundColor = 'white';
      } else {
        element.style.backgroundColor = 'lightgray';
      };
    });
  };

  const addEvents = function() {
    let playList = root.querySelectorAll('li');
    playList.forEach(function(element, index) {
      element.addEventListener('click', function(i) {
        highlight(index);
      });
    });
  };

  const clickHandler = function() {}
  const load = function() {

  }


  return {
    render: render,
    highlight: highlight,
    
  }
}

 

let playlistModule = Playlists();
// playlistModule.deleted();
playlistModule.highlight();

ajax('/playlists', playlistModule.render)
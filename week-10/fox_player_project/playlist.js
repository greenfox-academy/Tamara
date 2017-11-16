'use strict';

const Playlists = function() {

  const root = document.querySelector('.playlist');
  const playlistRoot = root.querySelector('ul');

  const render = function(data) {
    console.log(data)
    playlistRoot.innerHTML = "";
    data.forEach(function(element) {
      let li = document.createElement('li')
      li.textContent = element;
      playlistRoot.appendChild(li); 
    });
    addEvents();
  }

  const showCreateDialog = function(titleName) {

  };

  let buttonToAddName = document.querySelector('button');
  buttonToAddName.addEventListener('click', function() {
    create()
  });
  
  const create = function() {
    let addTitleName = document.querySelector('input');
    let newPost = {name: addTitleName.value}
    if (addTitleName.value !== '') {
      ajax('POST', '/playlists', newPost, render);
    };
  };

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
    ajax('GET', '/playlists', null, render);
  }

  return {
    render: render,
    highlight: highlight,
    create: create,
    load: load,
    showCreateDialog: showCreateDialog,

  }
}


let playlistModule = Playlists();
// playlistModule.deleted();
playlistModule.highlight();

ajax('GET', '/playlists', null, playlistModule.render)
playlistModule.create()
playlistModule.showCreateDialog()
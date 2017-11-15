'use strict';

const Playlists = function() {

  const root = document.querySelector('.playlist');
  const playlistRoot = root.querySelector('ul');
  // const fa = <i class="fa fa-times icon" aria-hidden="true"></i>;
  const render = function(data) {
    playlistRoot.innerHTML = "";
    data.forEach(function(element) {
      let li = document.createElement('li')
      li.textContent = element.title;
      root.appendChild(li);  
      // let xSign = document.createElement('i');
      // playlist.appendChild(xSign);
    });
    addEvents();
  }

  const showCreateDialog = function(titleName) {

  };
  
  const create = function(titleName) {
    let addTitleName = document.querySelector('input');
    let buttonToAddName = document.querySelector('button');
    if (addTitleName.value !== '') {
      buttonToAddName.addEventListener('click', function() {
        let newPost = {name: addTitleName.value}
        ajax('POST', '/playlists', newPost, render);
      });
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
    ajax('GET', render);
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
playlistModule.create('Best of')
playlistModule.showCreateDialog()
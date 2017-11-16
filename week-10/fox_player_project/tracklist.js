'use strict';

const Tracklists = function() {
  
    const root = document.querySelector('.playlisttosong');
    const tracklistRoot = root.querySelector('ul');
  
    const render = function(data) {
      console.log(data)
      tracklistRoot.innerHTML = "";
      data.forEach(function(element) {
        let li = document.createElement('li')
        li.textContent = element;
        tracklistRoot.appendChild(li); 
      });
      addEvents();
    }
  
    const showCreateDialog = function(data) {
      // ajax('POST', '/playlists/tracklist', data, create);
      // ajax('GET', '/playlists/tracklist', null, render);
    };
  
    // let buttonToShowList = document.querySelector('button');
    // buttonToShowList.addEventListener('click', function() {
    //   create()
    // });
    
    const create = function() {
      // let addTitleName = document.querySelector('input');
      // let newPost = {name: addTitleName.value}
      // if (addTitleName.value !== '') {
      //   ajax('POST', '/playlists', newPost, render);
      // };
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
      let trackList = root.querySelectorAll('li');    
      trackList.forEach(function(element, i) {
        if (index === i) {
          element.style.backgroundColor = 'lightblue';
        } else if (i % 2 === 0) {
          element.style.backgroundColor = 'darkgray';
        } else {
          element.style.backgroundColor = 'lightgray';
        };
      });
    };
  
    const addEvents = function() {
      let trackList = root.querySelectorAll('li');
      trackList.forEach(function(element, index) {
        element.addEventListener('click', function(i) {
          highlight(index);
        });
      });
    };
  
    const clickHandler = function() {}
    const load = function() {
      ajax('GET', '/playlists/tracklist', null, render);
    }
  
    return {
      render: render,
      highlight: highlight,
      create: create,
      load: load,
      showCreateDialog: showCreateDialog,
  
    }
  }
  
  
  let TracklistModule = Tracklists();
  // TracklistModule.deleted();
  TracklistModule.highlight();
  
  ajax('GET', '/playlists/tracklist', null, TracklistModule.render)
  TracklistModule.create()
  TracklistModule.showCreateDialog()
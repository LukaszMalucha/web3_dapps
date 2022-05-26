import React from 'react';
import ReactDOM from 'react-dom';
import YTSearch from 'youtube-api-search';

import SearchBar from './components/search_bar';




const YOUTUBE_KEY = process.env.YOUTUBE_KEY

YTSearch({key: YOUTUBE_KEY, term: 'surfboards'}, function(data) {
  console.log(data);
});


const App = () => {
  return (
    <div>
      <SearchBar />
    </div>
  );
}




ReactDOM.render(<App />, document.querySelector('.container'));


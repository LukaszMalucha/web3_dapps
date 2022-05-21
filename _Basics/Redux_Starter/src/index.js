import React from 'react';
import ReactDOM from 'react-dom';

import SearchBar from './components/search_bar';

const YOUTUBE_KEY = process.env.VUE_APP_YOUTUBE_KEY

const App = function() {
  return (
    <div>
      <SearchBar />
    </div>
  );
}




ReactDOM.render(<App />, document.querySelector('.container'));


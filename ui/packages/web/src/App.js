import React from 'react';
import { Route, Switch } from 'react-router-dom';
import Header from 'common/src/components/Header';
import Footer from 'common/src/components/Footer';
import Home from '../../common/src/pages/Home';
import Game from '../../common/src/pages/Game';
import About from '../../common/src/pages/About';

const App = () => {
  return (
    <div>
      <Header />
      <Switch>
        <Route exact path="/" component={Home} />
        <Route path="/game" component={Game} />
        <Route path="/about" component={About} />
      </Switch>
      <Footer />
    </div>
  );
};

export default App;

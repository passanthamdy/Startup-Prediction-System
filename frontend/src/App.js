import './App.css';
import {BrowserRouter as Router, Route, Switch} from 'react-router-dom';
import Home from './pages';
import SigninPage from './pages/signin';
import SignupPage from './pages/signup';
import PostsPage from './pages/posts';
import InvestorsPage from './pages/investors';
import Navbar from './components/NavBar';
import AddPostsPage from './pages/addpost';

function App() {
  return (
    <Router >
      <Switch>
        <Route path="/" component={Home} exact/>
        <Route path='/signin' component={SigninPage} exact/>
        <Route path="/signup" component={SignupPage} exact/>
        <Route path="/posts" component={PostsPage} exact/>
        <Route path="/investors" component={InvestorsPage} exact/>
        <Route path="/add" component={AddPostsPage} exact/>
      </Switch>
    </Router>
    
  );
}

export default App;

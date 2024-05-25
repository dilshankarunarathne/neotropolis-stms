import { BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import { About } from './components/pages/About';
import Home from './components/pages/Home';
import Login from './components/pages/Login';
import Navbar from './components/pages/Navbar';


function App() {
  return (
        <Router>
        <div>
          <Routes>
          <Route path="/" element={<Home />} />
         
          <Route path="/login">
            <Login/>
          </Route>

          <Route path="/About">
            <About/>
          </Route>
         
      </Routes>
      </div>
    </Router>
   
  );
}

export default App;
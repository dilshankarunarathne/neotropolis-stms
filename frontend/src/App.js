import { BrowserRouter as Router, Route, Routes, useNavigate, Switch} from 'react-router-dom';
import { useEffect } from 'react';
import AuthContext from './context/AuthProvider';
//import Register from './components/pages/Register';
import Login from './components/pages/Login';
import Home from './components/pages/Home'; 
import Navbar from './components/pages/Navbar';
//import Adduser from './components/pages/Adduser';
//import AddAdmin from './components/pages/AddAdmin';
//import UpdateUser from './components/pages/UpdateUser';
//import UpdateAdmin from './components/pages/UpdateAdmin';

function Default() {
  const navigate = useNavigate();
  useEffect(() => {
    navigate('/home');
  }, [navigate]);

  return null;
}

function App() {
  return (
      
      <main className="App">
        <Routes>
        <div>
          <Switch>
          <Route exact path="/">
            <Navbar/>
          </Route>
         
          <Route exact path="/signup">
            <SignUp/>
          </Route>
         
      </Switch>
      </div>
    </Routes>
            
    </main>
  );
}

export default App;
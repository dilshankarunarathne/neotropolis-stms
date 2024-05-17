import { BrowserRouter as Router, Route, Routes, useNavigate } from 'react-router-dom';
import { useEffect } from 'react';
import AuthContext from './context/AuthProvider';
import Register from './components/pages/Register';
import Login from './components/pages/Login';
import Home from './components/pages/Home'; 
import Adduser from './components/pages/Adduser';

function Default() {
  const navigate = useNavigate();
  useEffect(() => {
    navigate('/home');
  }, [navigate]);

  return null;
}

function App() {
  return (
    <Router>
      <main className="App">
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/home" element={<Home />} />
          <Route path="/" element={<Default />} />
          <Route path="/Adduser" element={<Adduser/>} />
        </Routes>
      </main>
    </Router>
  );
}

export default App;

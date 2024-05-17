import { BrowserRouter as Router, Route, Routes, useNavigate } from 'react-router-dom';
import { useEffect } from 'react';
import AuthContext from './context/AuthProvider';
import Register from './components/pages/SignUp';
import Home from './components/pages/Home'; 
import Login from './components/pages/Login';

function Default() {
  const navigate = useNavigate();
  useEffect(() => {
    navigate('/Navbar');
  }, [navigate]);

  return null;
}

function App() {
  return (
    <Router>
      <main className="App">
        <Routes>
          <Route path="./componrnts/pages/login" element={<Login />} />
          <Route path="/" element={<Default />} />
        </Routes>
      </main>
    </Router>
  );
}

export default App;

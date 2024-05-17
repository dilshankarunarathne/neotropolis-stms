import { BrowserRouter as Router, Route, Routes, useNavigate } from 'react-router-dom';
import { useEffect } from 'react';
import Login from './components/pages/Login';

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
          <Route path="./componrnts/pages/Login" element={<Login />} />
          <Route path="/" element={<Default />} />
        </Routes>
      </main>
    </Router>
  );
}

export default App;

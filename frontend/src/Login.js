import React, { useState } from 'react';
import { Link } from 'react-router-dom'; // Import Link from react-router-dom

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    // Here, you can make an API call to your backend to authenticate the user
    console.log('Login attempt:', username, password);
    // Handle the response
  };

    return (
      <div className="login-container">
        <h2>Login</h2>
        <form onSubmit={handleSubmit}>
          {/* ... form fields ... */}
        </form>
        <p>
          Don't have an account? <Link to="/register">Sign up now!</Link>
        </p>
      </div>
    );
  }

  export default Login;

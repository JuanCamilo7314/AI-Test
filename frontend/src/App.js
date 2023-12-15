import React, { useState } from 'react';
import axios from 'axios';
import './App.css'

const App = () => {
  const [inputText, setInputText] = useState('');
  const [summary, setSummary] = useState('');
  const [error, setError] = useState('');

  const handleInputChange = (e) => {
    setInputText(e.target.value);
  };

  const handleSummarizeClick = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:5000/resumir_texto', {
        texto: inputText,
      });

      setSummary(response.data.resumen_organizado);
      setError('');
    } catch (error) {
      setSummary('');
      setError('Error al procesar el texto. Por favor, intenta de nuevo.');
    }
  };

  return (
    <div class="container">
      <h1>Prueba Técnica - EDI - Resumen de Texto</h1>
      <textarea
        rows="10"
        cols="50"
        placeholder="Ingresa tu texto aquí..."
        value={inputText}
        onChange={handleInputChange}
      ></textarea>
      <br />
      <button onClick={handleSummarizeClick}>Resumir</button>
      <br />
      {summary && (
        <div class="summary-container">
          <h2>Resumen:</h2>
          <p>{summary}</p>
        </div>
      )}
      {error && <p class="error-message">{error}</p>}
    </div>
  );
};

export default App;
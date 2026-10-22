import "./App.css";

const address = "http://localhost:8000/ask"


function App() {

  async function answer(){
    const response = await fetch(address, {
      method: 'POST',
      body: JSON.stringify({question: "What is CORS?"}),
      headers: {'Content-Type': 'application/json'}
    })
    const data = await response.json()
    console.log(data)
  }

  return (
    <>
      <h1>fastapi.search</h1>
      <input></input>
      <button onClick = {answer} >Send</button>
      <div></div>
      <ul></ul>
    </>
  );
}

export default App;

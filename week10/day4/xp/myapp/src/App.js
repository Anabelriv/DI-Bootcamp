import Counter from './components/BuggyCounter';
import ErrorBoundary from './ErrorBoundary';
import Color from './components/Color';
import './App.css';

function App() {
  return (
    <div className="App">
      <h1>My first task</h1>
      <h4>Option 1</h4>
      <ErrorBoundary>
        <Counter /><br />
        <Counter /><br />
      </ErrorBoundary>
      <h4>Option 2</h4>
      <ErrorBoundary>
        <Counter /><br />
      </ErrorBoundary>
      <ErrorBoundary>
        <Counter /><br />
      </ErrorBoundary>
      <h4>Option 3</h4>
      <Counter />
      <h2>Task2</h2>
      <Color />


    </div>
  );
}

export default App;

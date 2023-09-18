import ErrorBoundary from './ErrorBoundary';
// import Counter from './component/Counter';
import { BrowserRouter, Routes, Route, NavLink } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import Profile from './components/Profile';
import Home from './components/Home';
import Shop from './components/Shop';
import PostList from './components/PostList';
import SocialMedias from './components/SocialMedias';
import Skills from './components/Skills';
import Experiences from './components/Experiences';
import './App.css';

// function App() {
//   return (
// <div>
//   <nav className='navbar navbar-expand-lg navbar-light bg-light'>
//     <div className='container'>
//       <NavLink className="navbar-brand" to="/">
//         Home
//       </NavLink>
//       <button
//         className="navbar-toggler"
//         type="button"
//         data-bs-toggle="collapse"
//         data-bs-target="#navbarNav"
//         aria-controls="navbarNav"
//         aria-expanded="false"
//         aria-label="Toggle navigation"
//       >
//         <span className="navbar-toggler-icon"></span>
//       </button>
//       <div className="collapse navbar-collapse" id="navbarNav">
//         <ul className="navbar-nav">
//           <li className="nav-item">
//             <NavLink className="nav-link" to="/profile">
//               Profile
//             </NavLink>
//           </li>
//           <li className="nav-item">
//             <NavLink className="nav-link" to="/shop">
//               Shop
//             </NavLink>
//           </li>
//         </ul>
//       </div>
//     </div>
//   </nav>

// <Routes>
//   <Route path="/" element={<ErrorBoundary><Home /></ErrorBoundary>} />
//   <Route path="/profile" element={<ErrorBoundary><Profile /></ErrorBoundary>} />
//   <Route path="/shop" element={
//     <ErrorBoundary>
//       <Shop />
//     </ErrorBoundary>} />

// </Routes>


// <>
//   <PostList />
// </>
//     <>
//       <SocialMedias />
//       <Skills />
//       <Experiences />
//     </>


//   );
// }

function App() {
  const webhookURL = "https://webhook.site/828cda39-70fd-479f-bd94-4678d03a234f";

  const sendRequestToWebhook = async () => {
    try {
      const data = {
        key1: "myusername",
        email: "mymail@gmail.com",
        name: "Isaac",
        lastname: "Doe",
        age: 27
      };

      const response = await fetch(webhookURL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });
      console.log(response)
    }
    catch (e) { console.log(e) }
  };
  return (
    <div className="App">
      <h1>Webhook</h1>
      <button onClick={sendRequestToWebhook}>Send Request to Webhook</button>
    </div>
  );
}

export default App;

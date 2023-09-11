import { Carousel } from 'react-responsive-carousel';
import "react-responsive-carousel/lib/styles/carousel.min.css"
import './App.css';
function App() {
  return (
    <div style={{ maxWidth: '600px', margin: '0 auto', maxHeight: '100px' }}>
      <Carousel>
        <div>
          <img src="https://cdn.britannica.com/75/156475-050-D97BBA64/Skyline-Hong-Kong.jpg" alt="Hong Kong" />
          <p className="legend">Hong Kong</p>
        </div>
        <div>
          <img src="./e8fnw35p6zgusq218foj.webp" alt='Las Vegas' />
          <p className="legend">Las Vegas</p>
        </div>
        <div>
          <img src="morocco.jpg" alt='Morocco' />
          <p className="legend">Morocco</p>
        </div>
        <div>
          <img src="/liw377az16sxmp9a6ylg.webp" alt='New York' />
          <p className="legend">New York</p>
        </div>
      </Carousel>
    </div>
  );
}

export default App;

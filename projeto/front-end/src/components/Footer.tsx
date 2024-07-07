import { FaInstagram, FaFacebook, FaTwitter } from 'react-icons/fa';

export default function Footer () {
  return (
    <footer className="bg-yellow-50 py-8">
      <div className="container mx-auto flex justify-between items-start px-4">
        <div className="flex flex-col items-start">
          <h2 className="text-2xl font-bold mb-4">App Delivery</h2>
          <address className="not-italic mb-4">
            Redenção, 1234 <br />
          </address>
          <div className="flex space-x-4">
            <a href="https://www.instagram.com" aria-label="Instagram" className="text-red-600 hover:text-gray-800">
              <FaInstagram size={24} />
            </a>
            <a href="https://www.facebook.com" aria-label="Facebook" className="text-red-600 hover:text-gray-800">
              <FaFacebook size={24} />
            </a>
            <a href="https://www.twitter.com" aria-label="Twitter" className="text-red-600 hover:text-gray-800">
              <FaTwitter size={24} />
            </a>
          </div>
        </div>

        <div className="flex flex-col">
          <h3 className="text-lg font-bold mb-2">Company</h3>
          <a href="#" className="text-gray-600 hover:text-gray-800 mb-1">About Us</a>
          <a href="#" className="text-gray-600 hover:text-gray-800 mb-1">Career</a>
          <a href="#" className="text-gray-600 hover:text-gray-800">How It Works</a>
        </div>

        <div className="flex flex-col">
          <h3 className="text-lg font-bold mb-2">Policy</h3>
          <a href="#" className="text-gray-600 hover:text-gray-800 mb-1">FAQ</a>
          <a href="#" className="text-gray-600 hover:text-gray-800 mb-1">Privacy</a>
          <a href="#" className="text-gray-600 hover:text-gray-800">Shipping</a>
        </div>

        <div className="flex flex-col">
          <h3 className="text-lg font-bold mb-2">Get In Touch</h3>
          <p className="text-gray-600 mb-1">+55 85 7311 2766</p>
          <p className="text-gray-600">appdelivery@example.com</p>
        </div>
      </div>

      <div className="container mx-auto text-center mt-8 px-4">
        <hr className="border-gray-300 mb-4"/>
        <p className="text-gray-600">&copy; 2022 Let’sFood. all rights reserved.</p>
      </div>
    </footer>
  );
}



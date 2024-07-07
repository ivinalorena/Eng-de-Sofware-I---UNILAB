export default function Header() {
  return (
    <header className="bg-red-500 text-yellow-400 p-4 flex justify-between items-center px-8 ">
      <h1 className="text-3xl font-bold">App Delivery</h1>
      <nav>
        <ul className="flex space-x-4">
          <li>
            <a href="/" className="hover:text-yellow-200">Home</a>
          </li>
          <li>
            <a href="#" className="hover:text-yellow-200">Menu</a>
          </li>
          <li>
            <a href="#" className="hover:text-yellow-200">Perfil</a>
          </li>
          <li>
            <a href="/login" className="hover:text-yellow-200">Login</a>
          </li>
        </ul>
      </nav>
    </header>
  )
}

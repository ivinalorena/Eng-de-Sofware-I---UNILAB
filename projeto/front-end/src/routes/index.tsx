import { RouterProvider, createBrowserRouter } from 'react-router-dom'
import { DefaultLayout } from '../layout'
import Home from '../pages/Home'
import Login from '../pages/Login'
import Register from '../pages/Register'


const router = createBrowserRouter([
    {
        path: '/',
        element: <DefaultLayout />,
        children: [
            {
                path: '/',
                element: <Home />
            }
        ],
    }
    , {
        path: '/login',
        element: <Login />
    },
    {
        path: '/register',
        element: <Register />
    }

])

export function Routes() {
    return <RouterProvider router={router} />
}
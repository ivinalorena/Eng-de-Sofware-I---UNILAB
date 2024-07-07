import { RouterProvider, createBrowserRouter } from 'react-router-dom'
import { DefaultLayout } from '../layout'
import Home from '../pages/Home'
import LoginPage from '../pages/Login'


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
        element: <LoginPage />
    }

])

export function Routes() {
    return <RouterProvider router={router} />
}
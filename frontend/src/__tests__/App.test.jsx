import { render, screen } from '@testing-library/react'
import App from '../App'

test('renders Vite + React heading', () => {
  render(<App />)
  const headingElement = screen.getByText(/Vite \+ React/i)
  expect(headingElement).toBeInTheDocument()
})

test('renders learn more link', () => {
  render(<App />)
  const linkElement = screen.getByText(/Click on the Vite and React logos to learn more/i)
  expect(linkElement).toBeInTheDocument()
})
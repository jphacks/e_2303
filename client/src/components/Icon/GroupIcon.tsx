import React from 'react'

type Props = {
  color: string
  size: number
}

export const GroupIcon: React.FC<Props> = ({ color, size }) => {
  return (
    <svg
      width={size}
      height={size}
      viewBox="0 0 48 48"
      fill="none"
      xmlns="http://www.w3.org/2000/svg">
      <mask maskUnits="userSpaceOnUse" x="0" y="0" width="48" height="48">
        <rect width="48" height="48" fill="#D9D9D9" />
      </mask>
      <g mask="url(#mask0_11_2178)">
        <path
          d="M0 36V32.85C0 31.4167 0.733333 30.25 2.2 29.35C3.66667 28.45 5.6 28 8 28C8.43333 28 8.85 28.0083 9.25 28.025C9.65 28.0417 10.0333 28.0833 10.4 28.15C9.93333 28.85 9.58333 29.5833 9.35 30.35C9.11667 31.1167 9 31.9167 9 32.75V36H0ZM12 36V32.75C12 31.6833 12.2917 30.7083 12.875 29.825C13.4583 28.9417 14.2833 28.1667 15.35 27.5C16.4167 26.8333 17.6917 26.3333 19.175 26C20.6583 25.6667 22.2667 25.5 24 25.5C25.7667 25.5 27.3917 25.6667 28.875 26C30.3583 26.3333 31.6333 26.8333 32.7 27.5C33.7667 28.1667 34.5833 28.9417 35.15 29.825C35.7167 30.7083 36 31.6833 36 32.75V36H12ZM39 36V32.75C39 31.8833 38.8917 31.0667 38.675 30.3C38.4583 29.5333 38.1333 28.8167 37.7 28.15C38.0667 28.0833 38.4417 28.0417 38.825 28.025C39.2083 28.0083 39.6 28 40 28C42.4 28 44.3333 28.4417 45.8 29.325C47.2667 30.2083 48 31.3833 48 32.85V36H39ZM8 26C6.9 26 5.95833 25.6083 5.175 24.825C4.39167 24.0417 4 23.1 4 22C4 20.8667 4.39167 19.9167 5.175 19.15C5.95833 18.3833 6.9 18 8 18C9.13333 18 10.0833 18.3833 10.85 19.15C11.6167 19.9167 12 20.8667 12 22C12 23.1 11.6167 24.0417 10.85 24.825C10.0833 25.6083 9.13333 26 8 26ZM40 26C38.9 26 37.9583 25.6083 37.175 24.825C36.3917 24.0417 36 23.1 36 22C36 20.8667 36.3917 19.9167 37.175 19.15C37.9583 18.3833 38.9 18 40 18C41.1333 18 42.0833 18.3833 42.85 19.15C43.6167 19.9167 44 20.8667 44 22C44 23.1 43.6167 24.0417 42.85 24.825C42.0833 25.6083 41.1333 26 40 26ZM24 24C22.3333 24 20.9167 23.4167 19.75 22.25C18.5833 21.0833 18 19.6667 18 18C18 16.3 18.5833 14.875 19.75 13.725C20.9167 12.575 22.3333 12 24 12C25.7 12 27.125 12.575 28.275 13.725C29.425 14.875 30 16.3 30 18C30 19.6667 29.425 21.0833 28.275 22.25C27.125 23.4167 25.7 24 24 24Z"
          fill={color}
        />
      </g>
    </svg>
  )
}

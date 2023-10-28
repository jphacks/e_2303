import { Config } from '../Config'

export const createGroup = async (name: string) => {
  console.log('createFroup', name)
  const data = await fetch(`${Config.ApiEndPoint}/group/`, {
    method: 'POST',
    headers: {
      accept: 'application/json',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      name,
    }),
  })
  return await data.json()
}

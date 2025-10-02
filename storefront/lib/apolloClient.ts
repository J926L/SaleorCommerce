// lib/apolloClient.ts

import { useMemo } from 'react'
import { ApolloClient, InMemoryCache, HttpLink } from '@apollo/client'

let apolloClient

function createApolloClient() {
  return new ApolloClient({
    ssrMode: typeof window === 'undefined', // 如果在服务器端则启用 SSR
    link: new HttpLink({
      uri: process.env.NEXT_PUBLIC_API_URL, // 从环境变量中获取 API URL
    }),
    cache: new InMemoryCache(),
  })
}

export function initializeApollo(initialState = null) {
  const _apolloClient = apolloClient ?? createApolloClient()

  // 如果有初始状态，则恢复它
  if (initialState) {
    _apolloClient.cache.restore(initialState)
  }

  // 对于 SSG 和 SSR，总是创建一个新的 Apollo Client
  if (typeof window === 'undefined') return _apolloClient
  // 在客户端，只在还没有实例的情况下创建一个
  if (!apolloClient) apolloClient = _apolloClient

  return _apolloClient
}

export function useApollo(initialState) {
  const store = useMemo(() => initializeApollo(initialState), [initialState])
  return store
}

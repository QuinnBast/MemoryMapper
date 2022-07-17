const routes = [
  {
    path: '/',
    component: () => import('layouts/NoMenuLayout.vue'),
    children: [
      { path: '', component: () => import('pages/EntryPage.vue') },
    ],
  },
  {
    path: '/memories',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/MemoryList.vue') },
    ],
  },
  {
    path: '/memory/:id',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/MemoryView.vue') },
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
  },
];

export default routes;

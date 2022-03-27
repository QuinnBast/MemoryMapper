<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />

        <q-toolbar-title>
          Memory Mapper
        </q-toolbar-title>

      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      bordered
    >
      <q-list>
        <q-item-label
          header
        >
          Essential Links
        </q-item-label>

        <EssentialLink
          v-for="link in essentialLinks"
          :key="link.title"
          v-bind="link"
        />
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { defineComponent, ref } from 'vue';
import EssentialLink from 'components/EssentialLink.vue';

const linksList = [
  {
    title: 'Account',
    caption: 'View account usage and settings',
    icon: 'person',
    link: '/account',
  },
  {
    title: 'About us',
    caption: 'Learn more about Memory Mapper',
    icon: 'info',
    link: '/about',
  },
  {
    title: 'Settings',
    caption: 'Turn the knobs and wheels',
    icon: 'settings',
    link: '/settings',
  },
  {
    title: 'Community',
    caption: 'Join the conversation!',
    icon: 'chat',
    link: '/chat',
  },
  {
    title: 'Developer?',
    caption: 'Fork our repository!',
    icon: 'code',
    link: 'https://github.com/QuinnBast/MemoryMapper',
  },
];

export default defineComponent({
  name: 'MainLayout',

  components: {
    EssentialLink,
  },

  setup() {
    const leftDrawerOpen = ref(false);

    return {
      essentialLinks: linksList,
      leftDrawerOpen,
      toggleLeftDrawer() {
        leftDrawerOpen.value = !leftDrawerOpen.value;
      },
    };
  },
});
</script>

<template>
<q-layout view="lHh Lpr lFf">
    <q-header elevated>
        <q-toolbar>
            <q-toolbar-title>
                EasyCounter
            </q-toolbar-title>
        </q-toolbar>
    </q-header>

    <q-page-container>
        <router-view />
    </q-page-container>
</q-layout>
</template>

<script>
export default {
    name: 'MainLayout'
}
</script>

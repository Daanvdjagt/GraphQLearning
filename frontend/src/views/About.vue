<template>
  <div class="about">
    <h1>This is an about page</h1>
    <UserList />
  </div>
</template>

<script>
import UserList from "../components/UserList";
export default {
  name: "about",
  components: {
    UserList
  }
};
</script>

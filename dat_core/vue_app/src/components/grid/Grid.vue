<template>
  <div class="cards">
    <div class="card" v-for="card in cards" v-bind:key="card.key">
      <div class="title">{{ card.title }}</div>
      <div class="description">{{ card.description }}</div>
      <div class="link">
        <a v-bind:href="card.href">{{ card.cta }}</a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "grid",
  props: ["cards"]
};
</script>

<style lang="scss">
</style>

<style lang="scss" scoped>
.cards {
  display: flex;
  flex-wrap: wrap;
}

.card {
  background: white;
  border: 1px solid #dcdfe6;
  border-radius: 6px;
  box-sizing: border-box;
  margin: 1rem 1rem;
  flex: 0 1 100%;
  padding: 2.5rem 1.8rem;
  display: flex;
  flex-direction: column;

  .title {
    font-size: 1.5rem;
    margin-bottom: 1rem;
  }
  .description {
    font-size: 1rem;
    line-height: 1.8rem;
    color: #303133;
  }
  .link {
    a {
      text-decoration: none;
      text-transform: uppercase;
      color: #8300bf;
    }
  }
}

@media screen and (min-width: 40em) {
  .card {
    flex: 0 1 calc(50% - 2em);
  }
}
@media screen and (min-width: 60em) {
  .card {
    flex: 0 1 calc(25% - 2em);
  }
}
</style>

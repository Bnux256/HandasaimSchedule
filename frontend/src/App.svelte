<script>
  // get list of classes
  let schedule = new Object();
  let classes = [];
  const url = "./schedule.json";
  fetch(url)
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      schedule = data;
      classes = Object.keys(schedule);
      classes.shift(); // removing first element - date
    });

  let cur_schedule = [];
  function get_schedule(chosen_class) {
    cur_schedule = schedule[chosen_class];

    // anlytics -
    const query = new URLSearchParams({
      p: "a0d80866-f248-4bf4-9e75-4dd1a01a4a52",
      i: chosen_class,
    });

    fetch(`https://app.piratepx.com/ship?${query.toString()}`);
  }
</script>

<main>
  <h1>מערכת שעות יומית - תיכון הנדסאים</h1>
  <h4>לקוח לא רשמי למערכת של תיכון הנדסאים הרצליה.</h4>
  <br />

  {#each classes as cur_class}
    <button on:click={get_schedule(cur_class)}>
      {cur_class}
    </button>
  {/each}

  <!-- print schedule -->
  <table class="center">
    <!-- print date -->
    {#if cur_schedule.length > 0}
      <tr>
        <th colspan="2">
          {schedule["date"]}
        </th>
      </tr>
    {/if}

    <!-- Print all lessons -->
    {#each cur_schedule as [i, lesson]}
      <tr>
        <th>{i}</th>
        {#if lesson !== null}
          <th>{lesson}</th>
        {/if}
      </tr>
    {/each}
  </table>

  <footer>
    <p>
      <a href="https://github.com/Bnux256/HandasaimSchedule">אודות הפרויקט</a>
    </p>
    <p>
      <a
        href="https://handasaim.co.il/2020/07/16/%d7%9e%d7%a2%d7%a8%d7%9b%d7%aa-%d7%99%d7%95%d7%9e%d7%99%d7%aa/"
        >קישור למערכת המקורית</a
      >
    </p>
  </footer>
</main>

<style>
  main {
    text-align: center;
    padding: 1em;
    margin: 0 auto;
  }

  h1 {
    color: #8400ff;
    text-transform: uppercase;
    font-size: 3em;
    font-weight: 100;
  }

  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }

  .center {
    margin-left: auto;
    margin-right: auto;
  }

  button {
    padding: 0.5em;
  }
</style>

<script>
  export let schedule, classes;
  async function download_schedule() {
    // get list of classes
    classes = [];
    const url = "./api/schedule";
    const data = await fetch(url, { cache: "no-store" });
    schedule = await data.json();
    classes = Object.keys(schedule);
    classes.shift(); // removing first element - date
  }

  download_schedule();
  setInterval(download_schedule, 5 * 60_000); // Refresh Schedule every 5 minutes
  export let cur_schedule = [];
  function get_schedule(chosen_class) {
    cur_schedule = schedule[chosen_class];
  }
</script>

<main>
  <h1>מערכת שעות יומית הנדסאים</h1>
  <p class="subtitle">מביא לכם את המערכת העדכנית של היום בצורה נוחה.</p>
  <p>
    <br />

    {#each classes as cur_class}
      <button on:click={get_schedule(cur_class)}>
        {cur_class}
      </button>
    {/each}

    <!-- print schedule -->
  </p>
  <table class="center">
    {#if typeof cur_schedule == "undefined"}
    <tr>
      <th colspan="2">
        המערכת בטעינה...
      </th>
    </tr>
    {/if}
    {#if typeof cur_schedule !== "undefined"}
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
          <td>{i}</td>
          {#if lesson !== null}
            <td>{lesson}</td>
          {/if}
        </tr>
      {/each}
    {/if}
  </table>

  <footer>
    <ul>
      <li><a href="https://github.com/Bnux256/HandasaimSchedule">אודות</a></li>
      <li>
        <a
          href="https://handasaim.co.il/2020/07/16/%d7%9e%d7%a2%d7%a8%d7%9b%d7%aa-%d7%99%d7%95%d7%9e%d7%99%d7%aa/"
          >למערכת המקורית</a
        >
      </li>
    </ul>
  </footer>
</main>

<style>
  :global(body) {
    padding-left: 0em;
    padding-right: 0em;
    padding-top: 2em;
    padding-bottom: 0em;
  }

  footer ul {
    list-style-type: none;
    display: inline-flex;
  }

  footer ul li {
    padding: 0em 1em;
  }

  main {
    text-align: center;
    margin: 0 auto;
  }

  h1 {
    color: #8400ff;
    font-size: 1.5em;
    font-weight: 100;
    padding: 0em 1em;
    font-family: sans-serif;
    margin: 0;
    margin-block-start: 0;
    margin-block-end: 0;
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

  p.subtitle {
    padding-top: 0em;
    padding-bottom: 0.2em;
    margin: 0em;
  }
</style>

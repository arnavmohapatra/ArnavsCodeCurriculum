import gpt_2_simple as gpt2

# gpt2.download_gpt2(model_name="124M")  # This could also be "124", `345M`, `774M`, or `1558M`

sess = gpt2.start_tf_sess()

gpt2.finetune(sess,
              "words.txt",
              model_name='124M',
              steps=1,
              restore_from='fresh',
              run_name='run1')
gpt2.load_gpt2(sess)
gpt2.generate(sess, length=100, temperature=0.7, prefix="hi mom ", nsamples=1)
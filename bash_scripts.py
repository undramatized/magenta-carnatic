'''
Different types of pretrained models
https://github.com/tensorflow/magenta/tree/master/magenta/models/melody_rnn

Basic
This configuration acts as a baseline for melody generation with an LSTM model. It uses basic one-hot encoding to represent extracted melodies as input to the LSTM. For training, all examples are transposed to the MIDI pitch range [48, 84] and outputs will also be in this range.

Mono
This configuration acts as a baseline for melody generation with an LSTM model. It uses basic one-hot encoding to represent extracted melodies as input to the LSTM. While basic_rnn is trained by transposing all inputs to a narrow range, mono_rnn is able to use the full 128 MIDI pitches.

Lookback
Lookback RNN introduces custom inputs and labels. The custom inputs allow the model to more easily recognize patterns that occur across 1 and 2 bars. They also help the model recognize patterns related to an events position within the measure. The custom labels reduce the amount of information that the RNN’s cell state has to remember by allowing the model to more easily repeat events from 1 and 2 bars ago. This results in melodies that wander less and have a more musical structure. For more information about the custom inputs and labels, and to hear some generated sample melodies, check out the blog post. You can also read through the events_to_input and events_to_label methods in magenta/music/encoder_decoder.py and magenta/music/melody_encoder_decoder.py to see how the custom inputs and labels are actually being encoded.

Attention
In this configuration we introduce the use of attention. Attention allows the model to more easily access past information without having to store that information in the RNN cell's state. This allows the model to more easily learn longer term dependencies, and results in melodies that have longer arching themes. For an overview of how the attention mechanism works and to hear some generated sample melodies, check out the blog post. You can also read through the AttentionCellWrapper code in Tensorflow to see what's really going on under the hood.
'''

# Basic RNN model with primer middle C
# 5 MIDI outputs

melody_rnn_generate \
--config=basic_rnn \
--bundle_file=./pretrained_models/basic_rnn.mag \
--output_dir=./tmp/melody_rnn/generated \
--num_outputs=5 \
--num_steps=128 \
--primer_melody="[60]"

# Basic RNN model with primer mohanam
melody_rnn_generate \
--config=basic_rnn \
--bundle_file=./pretrained_models/basic_rnn.mag \
--output_dir=./generated/mohanam_basic_rnn/ \
--num_outputs=3 \
--num_steps=256 \
--primer_midi=./raga_midi/mohanam_2.mid

# Lookback RNN model with primer mohanam
melody_rnn_generate \
--config=lookback_rnn \
--bundle_file=./pretrained_models/lookback_rnn.mag \
--output_dir=./generated/mohanam_lookback_rnn/ \
--num_outputs=3 \
--num_steps=256 \
--primer_midi=./raga_midi/mohanam_2.mid

# Attention RNN model with primer mohanam
melody_rnn_generate \
--config=attention_rnn \
--bundle_file=./pretrained_models/attention_rnn.mag \
--output_dir=./generated/mohanam_attention_rnn/ \
--num_outputs=3 \
--num_steps=256 \
--primer_midi=./raga_midi/mohanam_2.mid

# Attention RNN with midifile primer
melody_rnn_generate \
--config=attention_rnn \
--bundle_file=./pretrained_models/attention_rnn.mag \
--output_dir=./generated/kharahara_rnn/ \
--num_outputs=5 \
--num_steps=128 \
--primer_midi=./raga_midi/mohanam_1.mid

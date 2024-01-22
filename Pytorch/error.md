1.	RuntimeError: a leaf Variable that requires grad is being used in an in-place operation.


/share/apps/anaconda-ci/fgci-centos7-anaconda/software/anaconda/2021-03-tf2/e54ecce8/lib/python3.8/site-packages/torch/optim/lr_scheduler.py:154: 

UserWarning: The epoch parameter in `scheduler.step()` was not necessary and is being deprecated where possible. Please use `scheduler.step()` to step the scheduler. During the deprecation, if epoch is different from None, the closed form is used instead of the new chainable form, where available. Please open an issue if you are unable to replicate your use case: https://github.com/pytorch/pytorch/issues/new/choose.

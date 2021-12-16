from dataset_carla_rs import *
from dataset_fastec_rs import *

def Create_dataloader(opts):
    if opts.dataset_type=='Fastec':
        dataset = Dataset_fastec_rs(opts.dataset_root_dir, \
                                    seq_len=opts.seq_len, \
                                    load_optiflow=False, \
                                    load_1st_GS=opts.load_1st_GS, \
                                    load_middle_gs=True)

    if opts.dataset_type=='Carla':
        load_mask = True
        if opts.is_training:
            load_mask = False
        dataset = Dataset_carla_rs(opts.dataset_root_dir, \
                                    seq_len=opts.seq_len, \
                                    load_middle_gs=True, \
                                    load_flow=opts.load_gt_flow, \
                                    load_1st_GS=opts.load_1st_GS, \
                                    load_optiflow=False, \
                                    load_mask=load_mask, \
                                    load_depth=False)

    dataloader = torch.utils.data.DataLoader(dataset, 
                                            batch_size=opts.batch_sz, 
                                            shuffle=opts.shuffle_data, 
                                            num_workers=opts.batch_sz, 
                                            drop_last=True)
    return dataloader

